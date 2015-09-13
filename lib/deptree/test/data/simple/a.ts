import b = require("./b")  // another inlined comment
import c = require("./c")  /* here's an inlined comment */
import g_t = require("./g t") // space in file name

# this comment should be ignored

# following is a mismatched quote enclosure, it should
# be excluded.
import d = require('./d")

# These imports are to be ignored, since they don't begin
# with ./ or ../
import x = requires("x")
import y = requires(".../y")
import z = requires("sub/z")
