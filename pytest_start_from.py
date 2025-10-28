"""
pytest plugin to start test execution from a specific test case.
All tests before the matched test will be skipped.
"""
import pytest
import re


class StartFromPlugin:
    """
    Plugin to control test execution starting point.
    """
    
    def __init__(self, start_from_pattern):
        self.start_from_pattern = start_from_pattern
        self.start_execution = False
        self.pattern_regex = None
        
        if start_from_pattern:
            # convert pattern to regex similar to pytest -k option
            self.pattern_regex = self._convert_pattern_to_regex(start_from_pattern)
    
    def _convert_pattern_to_regex(self, pattern):
        """
        convert user pattern to regex for matching test names
        similar to pytest -k behavior
        """
        # handle 'and', 'or', 'not' keywords
        if ' and ' in pattern or ' or ' in pattern or ' not ' in pattern:
            # for complex patterns, use simple contains check
            return None
        
        # for simple pattern, treat as substring match
        return re.compile(re.escape(pattern))
    
    def _matches_pattern(self, nodeid):
        """
        check if test nodeid matches the start pattern
        """
        if not self.start_from_pattern:
            return False
        
        # extract test name from nodeid
        # nodeid format: path/to/test_file.py::TestClass::test_method or path/to/test_file.py::test_function
        test_name = nodeid.split("::")[-1]
        full_name = nodeid
        
        # handle complex patterns with keywords
        if ' and ' in self.start_from_pattern or ' or ' in self.start_from_pattern or ' not ' in self.start_from_pattern:
            return self._evaluate_complex_pattern(test_name, full_name)
        
        # simple substring match
        if self.pattern_regex:
            return (self.pattern_regex.search(test_name) is not None or 
                    self.pattern_regex.search(full_name) is not None)
        
        return (self.start_from_pattern in test_name or 
                self.start_from_pattern in full_name)
    
    def _evaluate_complex_pattern(self, test_name, full_name):
        """
        evaluate complex pattern with 'and', 'or', 'not' keywords
        """
        pattern = self.start_from_pattern
        
        # replace keywords with python operators
        pattern = pattern.replace(' and ', ' and ')
        pattern = pattern.replace(' or ', ' or ')
        pattern = pattern.replace(' not ', ' not ')
        
        # extract all words (potential substrings to match)
        words = re.findall(r'\b(?:and|or|not)\b|\S+', pattern)
        
        # build evaluation expression
        eval_expr = []
        for word in words:
            if word in ['and', 'or', 'not']:
                eval_expr.append(word)
            else:
                # check if word is in test_name or full_name
                match = (word in test_name or word in full_name)
                eval_expr.append(str(match))
        
        try:
            return eval(' '.join(eval_expr))
        except Exception:
            # fallback to simple contains check
            return self.start_from_pattern in test_name or self.start_from_pattern in full_name
    
    @pytest.hookimpl(tryfirst=True)
    def pytest_runtest_setup(self, item):
        """
        hook called before each test execution
        skip tests before the start pattern is matched
        """
        if not self.start_from_pattern:
            return
        
        if not self.start_execution:
            if self._matches_pattern(item.nodeid):
                # found the starting test, enable execution from now on
                self.start_execution = True
                return
            else:
                # skip this test as we haven't reached the start point yet
                pytest.skip(f"Skipped: execution starts from '{self.start_from_pattern}'")


def pytest_addoption(parser):
    """
    add command line options for the plugin
    """
    parser.addoption(
        '--start-from',
        action='store',
        default=None,
        help='Start test execution from the first test matching this pattern (similar to -k). '
             'All tests before the matched test will be skipped. '
             'Supports substring matching and keywords: and, or, not'
    )


def pytest_configure(config):
    """
    register the plugin with pytest
    """
    start_from = config.getoption('start_from')
    
    if start_from:
        plugin = StartFromPlugin(start_from)
        config.pluginmanager.register(plugin, 'start_from_plugin')
        
        # add marker documentation
        config.addinivalue_line(
            'markers',
            'start_from: mark where test execution should start from'
        )
