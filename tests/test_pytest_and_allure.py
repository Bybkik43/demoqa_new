import allure
import pytest

@allure.title('пропущенный текст')
@pytest.mark.skip(reason= 'причина пропуска')
def test_skip():
    assert True

@pytest.mark.xfail(condition=True, reason='причина, по которой тестова функция помечена как xfail')
def test_xfail_1():
    assert False

@pytest.mark.xfail(condition=True, reason='причина, по которой тестова функция помечена как xfail')
def test_xfail_1():
    assert True

@pytest.mark.skipif(condition='2 + 2!= 5')
def test_skip_by_triggired_condition():
    pass
@pytest.mark.parametrize('param', [1, 2, 3, 4, 6])
def test_parametrize(param):
    assert (param % 2) == 0

