from library_system.member import Member

def test_member_limit():
    member = Member("Test", "M1")
    for i in range(5):
        member.borrow_book(str(i))
    assert not member.can_borrow()
