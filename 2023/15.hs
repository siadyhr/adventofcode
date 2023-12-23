--{-# OPTIONS_GHC -Wall #-}
module Main
    where

import Data.Map (Map)
import qualified Data.Map as Map
import Data.Char (ord)
import MyAOCLib

parse :: String -> [[Int]]
parse rawInput = map (map ord) (split ',' rawInput)

hashStep :: Int -> Int -> Int
hashStep current new = ((current + new)*17) `mod` 256

hash :: [Int] -> Int
hash = foldl hashStep 0

part1 x = sum $ map hash (parse x)
part2 rawInput = Map.foldrWithKey (\key val start -> start + (boxScore key val)) 0 boxes
    where
        boxes = foldl updateBoxes (Map.empty) instructions
        instructions = split ',' rawInput

        boxScore :: Int -> [(String, Int)] -> Int
        boxScore boxNumber boxContents = (boxNumber + 1) * (boxContentScore boxContents)

        boxContentScore :: [(String, Int)] -> Int
        boxContentScore x = boxContentScore' 1 (reverse x)
            where
                boxContentScore' :: Int -> [(String, Int)] -> Int
                boxContentScore' _ [] = 0
                boxContentScore' n ((_,value):elements) = (n*value) + boxContentScore' (n+1) elements

part1OneLine :: String -> Int
part1OneLine x = sum $ map (foldl (\a b -> ((a + b :: Int)*17 `mod` 256)) 0) (map (map ord) (split ',' x))

updateBoxes :: Map Int [(String, Int)] -> String -> Map Int [(String, Int)]
updateBoxes boxes rawInstruction
    -- First case er forkert; hvis nøglen findes skal værdien opdateres uden at listen ændres
    | instruction == "="    = insertLens boxes (label, number)
    | instruction == "-"    = Map.insert labelId ([(x,y) | (x, y) <- existingLenses, x /= label]) boxes
    where
        label = [x | x <- rawInstruction, x `elem` ['a'..'z']]
        instruction = [x | x <- rawInstruction, x `elem` "=-"]
        number = [x | x <- rawInstruction, x `elem` ['0'..'9']]
        labelId = hash $ map ord label

        existingLenses = Map.findWithDefault [] labelId boxes
        
        insertLens boxes (label, number)
            | lensExists    = Map.insert labelId (replaceLens boxContent (label, read number :: Int)) boxes
            | otherwise     = Map.insertWith (++) labelId [(label, read number :: Int)] boxes
            where
                replaceLens content (label, number) = [(x,y_new) | (x, y) <- content, let y_new = if x == label then number else y]
                lensExists = label `elem` (map fst boxContent)
                boxContent = Map.findWithDefault [] labelId boxes

main = do
    rawSampleInput <- (readLines "15sample.in")
    rawInput <- (readLines "15.in")

    putStrLn "Part 1"
    putStrLn $ show $ part1 $ head rawSampleInput
    putStrLn $ show $ part1 $ head rawInput
    putStrLn $ show $ part1OneLine $ head rawInput

    putStrLn "Part 2"
--    putStrLn $ show $ foldl updateBoxes (Map.empty) ["rn=1","cm-","qp=3","cm=2","qp-","pc=4","ot=9","ab=5","pc-","pc=6","ot=7"]

    putStrLn $ show $ part2 $ head rawSampleInput
    putStrLn $ show $ part2 $ head rawInput
