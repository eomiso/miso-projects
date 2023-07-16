-- All plugins have lazy=true by default, to load a plugin on startup just lazy=false
-- List of all default plugins & their definitions

local default_plugins = {

	-- file managing, picker etc
	{
		"nvim-tree/nvim-tree.lua",
		cmd = { "NvimTreeToggle", "NvimTreeFocus" },
		dependencies = {
			"nvim-tree/nvim-web-devicons",
		},
		opts = function()
			return require "plugins.nvimtree.config"
		end,
		config = function(_, opts)
			require("nvim-tree").setup {}
			vim.g.nvimtree_side = opts.view.side
		end,
	}
}
