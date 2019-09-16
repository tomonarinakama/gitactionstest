import testtools

from gitactionstest import dummy

class DummyTest(testtools.TestCase):

  def test_dummy(self):
    d = dummy.Dummy()
    ret = d.one_plus_one()
    self.assertEqual(2, ret)
