local g = vim.g

-------------------------------------- globals ----------------------------------------
-- This directory is needed for using NvChad/base46
-- Take a look at the code linked below:
--   https://github.com/NvChad/base46/blob/bad87b034430b0241d03868c3802c2f1a4e0b4be/lua/base46/init.lua#L127-L142
-- It writes the base46 color tables extensions for each plugins to the `base64_cache`
-- This will happen when the `load_all_highlights` function is called. The `M.complie` function does this.
--   https://github.com/NvChad/base46/blob/bad87b034430b0241d03868c3802c2f1a4e0b4be/lua/base46/init.lua#L121-L145
g.base46_cache = vim.fn.stdpath "data" .. "/nvchad/base46/"
