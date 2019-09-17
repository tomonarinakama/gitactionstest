import testtools

from gitactionstest import dummy

class DummyTest(testtools.TestCase):

  def test_one_plus_one(self):
    d = dummy.Dummy()
    ret = d.one_plus_one()
    self.assertEqual(2, ret)

  def test_one_plus_two(self):
    d = dummy.Dummy()
    ret = d.one_plus_two()
    self.assertEqual(3, ret)
