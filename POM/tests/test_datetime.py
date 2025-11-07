import  datetime
def test_date_comparison():
    today = datetime.now(); tomorrow = today + timedelta(days=1)
    assert tomorrow > today

def test_timezone_conversion():
    utc = datetime.utcnow(); local = datetime.now()
    assert abs((local - utc).total_seconds()) < 3600

def test_date_format():
    assert datetime(2025, 11, 4).strftime("%Y-%m-%d") == "2025-11-04"

def test_age_calculation():
    birth = datetime(2000, 1, 1); today = datetime(2025, 11, 4)
    age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
    assert age == 25
