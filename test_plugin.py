"""
Unit tests for pytest-start-from plugin
"""
import pytest


def test_plugin_loaded(pytestconfig):
    """verify that the plugin is properly loaded"""
    plugin_names = []
    for p in pytestconfig.pluginmanager.get_plugins():
        if hasattr(p, '__module__'):
            plugin_names.append(p.__module__)
        elif hasattr(p, '__name__'):
            plugin_names.append(p.__name__)
    assert 'pytest_start_from' in plugin_names


def test_start_from_option_available(pytestconfig):
    """verify that --start-from option is available"""
    # check if the option exists
    option = pytestconfig.option
    assert hasattr(option, 'start_from')


class TestPatternMatching:
    """test pattern matching logic"""
    
    def test_simple_match(self):
        """test simple pattern matching"""
        from pytest_start_from import StartFromPlugin
        
        plugin = StartFromPlugin("test_third")
        
        # should match
        assert plugin._matches_pattern("test_example.py::test_third")
        
        # should not match
        assert not plugin._matches_pattern("test_example.py::test_first")
    
    def test_substring_match(self):
        """test substring pattern matching"""
        from pytest_start_from import StartFromPlugin
        
        plugin = StartFromPlugin("third")
        
        # should match
        assert plugin._matches_pattern("test_example.py::test_third")
        
        # should not match
        assert not plugin._matches_pattern("test_example.py::test_first")
    
    def test_class_method_match(self):
        """test matching class methods"""
        from pytest_start_from import StartFromPlugin
        
        plugin = StartFromPlugin("test_class_second")
        
        # should match
        assert plugin._matches_pattern("test_example.py::TestClass::test_class_second")
        
        # should not match
        assert not plugin._matches_pattern("test_example.py::TestClass::test_class_first")
    
    def test_no_pattern(self):
        """test behavior when no pattern is specified"""
        from pytest_start_from import StartFromPlugin
        
        plugin = StartFromPlugin(None)
        
        # should not match anything
        assert not plugin._matches_pattern("test_example.py::test_any")


class TestExecutionControl:
    """test execution control logic"""
    
    def test_start_execution_flag(self):
        """test that execution flag is set correctly"""
        from pytest_start_from import StartFromPlugin
        
        plugin = StartFromPlugin("test_third")
        
        # initially, execution should not start
        assert not plugin.start_execution
        
        # after matching, execution should start
        plugin._matches_pattern("test_example.py::test_third")
        plugin.start_execution = True
        assert plugin.start_execution
