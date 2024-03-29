{-# OPTIONS_GHC -Wall #-}
module Main
    where

import MyAOCLib

parse :: [String] -> [(String, [Int])]
parse = map parseLine
    where
        parseLine :: String -> (String, [Int])
        parseLine line = (symbols, numbers)
            where
                [symbols, rawNumbers] = split ' ' line
                numbers = map read $ split ',' rawNumbers

countSpringConfigurations :: (String, [Int]) -> Int
countSpringConfigurations ("", l)
    | null l    = 1
    | otherwise = 0
countSpringConfigurations (xs, [])
    | '#' `elem` xs = 0
    | otherwise     = 1
-- Case: Flere instruktioner. Needs a at least instruction+2 space
countSpringConfigurations (xs, instruction:instruction2:instructions)
    | length xs < instruction + 2   = 0
countSpringConfigurations (xs, [instruction])
    | instruction > length xs   = 0
    | (instruction == length xs) && (all (`elem` "#?") xs)  = 1
    | (instruction == length xs) = 0
-- Case 3 here is if xs contains some '.', but the instruction
-- needs them all to be # or ?.

{- To take 'instruction' many #'s, we need
 - exactly (instruction-1) #'s in xs and that
 - xs!!(instruction-1) is '.'. In that case we
 - eat x, (instruction-1) #'s and a '.'
 -}

countSpringConfigurations (x:xs, instruction:instructions)
    | x == '.'      = countSpringConfigurations (xs, (instruction:instructions))
    | (x == '#')    = if (all (`elem` "#?") $ take (instruction-1) xs) && (xs!!(instruction-1) `elem` ".?") then
                        countSpringConfigurations (drop instruction xs, instructions)
                        else 0
    | x == '?'      = (countSpringConfigurations ('.':xs, instruction:instructions))
                        + (countSpringConfigurations ('#':xs, instruction:instructions))

part1 l = sum $ map countSpringConfigurations l

multiplyInput :: [(String, [Int])] -> [(String, [Int])]
multiplyInput lines = map multiplyInputLine lines
    where
        multiplyInputLine (xs, instructions) = (repeatXs, repeatInstructions)
            where
                repeatXs = tail $ foldl (++) "" (take 5 $ repeat ('?':xs))
                repeatInstructions = foldl (++) [] (take 5 $ repeat instructions)
                

part2 = part1 . multiplyInput

main = do
    rawSampleInput <- (readLines "12sample.in")
    rawInput <- (readLines "12.in")

    putStrLn "Hello, World!"
    putStrLn $ show $ part1 $ parse $ rawSampleInput
    putStrLn $ show $ part1 $ parse $ rawInput
    putStrLn "Part 2"
    putStrLn $ show $ part2 $ parse $ rawSampleInput
    putStrLn $ show $ part2 $ parse $ rawInput
