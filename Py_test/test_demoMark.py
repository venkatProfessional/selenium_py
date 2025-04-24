# how to mark a test cases wih specific name
import pytest


@pytest.mark.smoke
def test_validate_YT_videos():
    youtubeVideo = "Running"
    assert  youtubeVideo=="Running","you tube video not running which smoke test is failed"

# mark as a skip will skip the test case

# 1 skipped
@pytest.mark.skip
def test_skipexample():
    print("Test case Skipped")

    # running the testcase but it is not reporting


# Why use xfail?
# When a bug is known but not fixed yet.
# When you are developing a feature and the test is expected to fail temporarily.
# To avoid test noise in the report for known issues.
@pytest.mark.xfail
def test_Markasfail_notreporting():
    print("test case will be executed but not reported")