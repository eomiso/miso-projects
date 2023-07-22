local M = {}
local merge_tb = vim.tbl_deep_extend

-- merge custom and core configs
M.load_config = function()
  local config = require "core/config"
  local misovimrc_path = vim.api.nvim_get_runtime_file("lua/custom/misovimrc.lua", false)

  if next(misovimrc_path) ~= nil then
    print("[DEBUG]")
    print("misovimrc_path is not nil!")
    local misovimrc = dofile(misovimrc_path[1])

    config.mappings = M.remove_disabled_keys(config.mappings, misovimrc.mappings)
    config = merge_tb("force", config, misovimrc_path)
    config.mappings.disabled = nil
  end

  print("[DEBUG]")
  print(config)

  return config
end

M.remove_duplicate_keys = function(target_mappings, custom_mappings)
  if not custom_mappings then
    return target_mappings
  end

  -- store keys in a array with true value to compare
  local keys_to_disable = {}
  for _, mappings in pairs(custom_mappings) do
    for mode, section_keys in pairs(mappings) do
      if not keys_to_disable[mode] then
        keys_to_disable[mode] = {}
      end
      section_keys = (type(section_keys) == "table" and section_keys) or {}
      for k, _ in pairs(section_keys) do
        keys_to_disable[mode][k] = true
      end
    end
  end

  -- make a copy as we need to modify target_mappings
  for section_name, section_mappings in pairs(target_mappings) do
    for mode, mode_mappings in pairs(section_mappings) do
      mode_mappings = (type(mode_mappings) == "table" and mode_mappings) or {}
      for k, _ in pairs(mode_mappings) do
        -- if key if found then remove from target_mappings
        if keys_to_disable[mode] and keys_to_disable[mode][k] then
          -- overlapping the target_mappings with the custom mappings.
          -- this makes the keys empty in the target_mappings so that merging the two tables work
          target_mappings[section_name][mode][k] = nil
        end
      end
    end
  end

  return target_mappings
end

return M
