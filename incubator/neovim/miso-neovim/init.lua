require "core"

-- Additional Settings
local custom_init_path = vim.api.nvim_get_runtime_file("lua/custom/init.lua", false)

local next = next

if next(custom_init_path) ~= nil then
	dofile(custom_init_path)
end

local lazypath = vim.fn.stdpath "data" .. "/lazy/lazy.nvim"

-- bootstrap lazy.nvim
if not vim.loop.fs_stat(lazypath) then
	require("core.bootstrap").lazy(lazypath)
end

--dofile(vim.g.base46_cache .. "defaults")
vim.opt.rtp:prepend(lazypath)
require "plugins"