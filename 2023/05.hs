--{-# OPTIONS_GHC -Wall #-}
module Main
    where

import Data.Map (Map)
import qualified Data.Map as Map
import MyAOCLib

translateOnce :: [(Int, Int, Int)] -> Int -> Int
translateOnce [] x = x
translateOnce ((startOut, startIn, rangeLength):xs) x
    |  xContained   = startOut + (x - startIn)
    | otherwise     = translateOnce xs x
    where
        xContained = (startIn <= x) && (x < startIn + rangeLength)

translate :: [[(Int, Int, Int)]] -> Int -> Int
translate [] x = x
translate (y:ys) x = translate ys (translateOnce y x)

parse :: [String] -> ([Int], [[(Int, Int, Int)]])
parse s = (seeds, maps)
    where
        seeds = parseSeeds rawSeeds
        maps = [map parseTriple x | x <- map tail rawMaps ]
        (rawSeeds:rawMaps) = split [] s
        parseTriple :: String -> (Int, Int, Int)
        parseTriple s' = (x, y, z)
            where [x,y,z] = map read (split ' ' s')
        parseSeeds :: [String] -> [Int]
        parseSeeds [x] = map read actualSeeds
            where actualSeeds = tail $ split ' ' x

seedPairsToSeeds :: [Int] -> [Int]
seedPairsToSeeds [] = []
seedPairsToSeeds (x:y:xys) = [x..x+y] ++ seedPairsToSeeds xys

minimalTranslation :: ([Int], [[(Int, Int, Int)]]) -> Int
minimalTranslation (seeds, maps) = minimum translations
    where
        translations = map (translate maps) seeds

part1 :: [String] -> Int
part1 s = minimalTranslation (seeds, maps)
    where
        (seeds, maps) = parse s

part2 :: [String] -> Int
part2 s = minimalTranslation ((seedPairsToSeeds $ seeds), maps)
    where
        (seeds, maps) = parse s

main = do
    rawInput <- (readLines "05.in")
    putStrLn "Hello, World!"
    putStrLn $ show $ part1 rawInput
    putStrLn $ show $ part2 rawInput
