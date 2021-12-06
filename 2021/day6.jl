function inc(dict, key, amount)
    if key in keys(dict)
        dict[key] += amount
    else
        dict[key] = amount
    end
end

function day(ages)
    new_ages = Dict{BigInt, BigInt}()
    for key in keys(ages)
        if key == 0
            inc(new_ages, 6, ages[key])
            inc(new_ages, 8, ages[key])
        else
            inc(new_ages, key - 1, ages[key])
        end
    end
    return new_ages
end

function total(ages)
    ret = 0
    for key in keys(ages)
        ret += ages[key]
    end
    return ret
end

INFILE = "day6.in"
open(INFILE) do f
    ages = Dict{BigInt, BigInt}()
    line = readline(f)
    start_timers = map(split(line, ",")) do x
        parse(BigInt, x)
    end
    for timer in start_timers inc(ages, timer, 1) end
    for _ in 1:80
        ages = day(ages)
    end
    println(total(ages)) # solA
    for _ in 1:176
        ages = day(ages)
    end
    println(total(ages)) # solB
end
