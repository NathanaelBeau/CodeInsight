str0 = "Convert [$this] [str!ng] into [n@st3d] [l!sts]"
expected_output = [['$this'], ['str!ng'], ['n@st3d'], ['l!sts']]
assert test(str0) == expected_output, 'Test failed'