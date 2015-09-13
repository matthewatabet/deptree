import b = require("./b")  // another inlined comment
import c = require("./c")  /* here's an inlined comment */

# this comment should be ignored

# following is a mismatched quote enclosure, it should
# be excluded.
import d = require('./d")
