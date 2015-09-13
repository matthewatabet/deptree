# test a missing reference
import b = require("./b")

# this file is missing too, but we want to check that the extension
# is not added twice.
import c = require("./c.ts")
