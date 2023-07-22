require "core"

-- Additional Settings
local custom_init_path = vim.api.nvim_get_runtime_file("lua/custom/init.lua", false)

local next = next

if next(custom_init_path) ~= nil then
  dofile(custom_init_path[1])
end

local lazypath = vim.fn.stdpath "data" .. "/lazy/lazy.nvim"

-- bootstrap lazy.nvim
if not vim.loop.fs_stat(lazypath) then
  require("core.bootstrap").lazy(lazypath)
end

-- This line should only be available when base46 plugin is downloaded
-- dofile(vim.g.base46_cache .. "defaults")

vim.opt.rtp:prepend(lazypath)
local default_plugins = require "plugins"

local configs = require("core.utils").load_config()

require("lazy").setup(default_plugins, configs.lazy_nvim)
