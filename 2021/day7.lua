local input = io.read("*all")

local function scoreA(nums, count, x)
  local total = 0
  for j=0,count-1 do
    total = total + math.abs(x - nums[j])
  end
  return total
end

local function scoreB(nums, count, x)
  local total = 0
  for j=0,count-1 do
    local n = math.abs(x - nums[j])
    total = total + (n * (n + 1) / 2)
  end
  return total
end

-- score(x) = sum_p abs(x-p)
local function sol(scorefn)
  local res = string.gmatch(input, "([0-9]+),*")
  local nums = {}
  local count = 0
  local minval = 99999
  local maxval = 0
  for r in res do
    local num = tonumber(r)
    if num < minval then
      minval = num
    end
    if num > maxval then
      maxval = num
    end

    nums[count] = num -- I know, it's 0-indexed, apologies
    count = count + 1
  end
  local bestpos = 0
  local bestscore = 99999999999
  for x=minval,maxval do
    local s = scorefn(nums, count, x)
    if s < bestscore then
      bestpos = x
      bestscore = s
    end
  end
  print(bestscore)
end

sol(scoreA)
sol(scoreB)
