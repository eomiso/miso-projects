local M = {}
local api = vim.api
local opt_local = vim.opt_local

local function screen()

-- Show nice welcome note after initial openning
  local text_on_screen = {


"  ____ ____ ____ ____ ____ ____ ____ _________ ____ ____  ",
" ||W |||e |||l |||c |||o |||m |||e |||       |||T |||o ||",
" ||__|||__|||__|||__|||__|||__|||__|||_______|||__|||__||",
" |/__\\|/__\\|/__\\|/__\\|/__\\|/__\\|/__\\|/_______\\|/__\\|/__\\|",
"  ____ ____ ____ ____ ____ ____ ____                     ",
" ||M |||i |||s |||o |||V |||i |||m ||                    ",
" ||__|||__|||__|||__|||__|||__|||__||                    ",
" |/__\\|/__\\|/__\\|/__\\|/__\\|/__\\|/__\\|                    ",
"                                                         ",
    "",
    "  This has mainly been inspired by NvChad a fast, lightweight ui config for neovim",
    "",
    "  If you dont see any syntax highlighting not working, install a tsparser for it",
    "",
    "  Check the default mappings by pressing space + ch or Cheatsheet command",
    "",
    "Now quit nvim!",
  }

  local buf = api.nvim_create_buf(false, true)

  vim.opt_local.filetype = "nvchad_postbootstrap_window"
  api.nvim_buf_set_lines(buf, 0, -1, false, text_on_screen)

  local nvpostscreen = api.nvim_create_namespace "nvpostscreen"

  for i = 1, #text_on_screen do
    api.nvim_buf_add_highlight(buf, nvpostscreen, "LazyCommit", i, 0, -1)
  end

  api.nvim_win_set_buf(0, buf)

  -- buf only options
  opt_local.buflisted = false
  opt_local.modifiable = false
  opt_local.number = false
  opt_local.list = false
  opt_local.relativenumber = false
  opt_local.wrap = false
  opt_local.cul = false
end

local function post_bootstrap()
  api.nvim_buf_delete(0, { force = true }) -- close previously opened lazy window

  vim.schedule(function()
    vim.cmd "MasonInstallAll"

    -- Keep track of which mason pkgs get installed
    local packages = table.concat(vim.g.mason_binaries_list, " ")

    require("mason-registry"):on("package:install:success", function(pkg)
      packages = string.gsub(packages, pkg.name:gsub("%-", "%%-"), "") -- rm package name

      -- run above screen func after all pkgs are installed.
      if packages:match "%S" == nil then
        vim.schedule(function()
          api.nvim_buf_delete(0, { force = true })
          vim.cmd "echo '' | redraw" -- clear cmdline
          screen()
        end)
      end
    end)
  end)
end

local function shell_call(args)
  local output = vim.fn.system(args)
  assert(vim.v.shell_error == 0, "External call failed with error code: " .. vim.v.shell_error .. "\n" .. output)
end

M.echo = function(str)
  vim.cmd "redraw"
  vim.api.nvim_echo({ { str, "Bold" } }, true, {})
end

M.lazy = function(install_path)
  --------- lazy.nvim ---------------
  M.echo "  Installing lazy.nvim & plugins ..."
  local repo = "https://github.com/folke/lazy.nvim.git"
  shell_call { "git", "clone", "--filter=blob:none", "--branch=stable", repo, install_path }
  vim.opt.rtp:prepend(install_path)

  -- install plugins
  require("plugins")

  -- mason packages & show post_bootstrap screen
  -- post_bootstrap()
	screen()
end

return M
