--{-# OPTIONS_GHC -Wall #-}
module Main
    where

import Data.Map (Map)
import qualified Data.Map as Map
import MyAOCLib

duplicateEmptyRows :: [String] -> [String]
duplicateEmptyRows [] = []
duplicateEmptyRows (row:rows)
    | all (=='.') row   = row:row:rest
    | otherwise         = row:rest
    where rest = duplicateEmptyRows rows

{- M^T is the head of every row,
 - followed by the transpose of the tails.
 -}
transpose :: [[a]] -> [[a]]
transpose [] = []
transpose matrix
    | (length $ head matrix) == 1   = [[x | [x] <- matrix]]
    | otherwise = (map head matrix):(transpose $ map tail matrix)

expandSpace :: [String] -> [String]
expandSpace s = transpose $ duplicateEmptyRows $ transpose $ duplicateEmptyRows s

getEmptyRows' :: (Eq a) => a -> Int -> [[a]] -> [Int]
getEmptyRows' _ _ [] = []
getEmptyRows' emptyChar lineNum (line:lines)
    | all (==emptyChar) line    = lineNum:rest
    | otherwise                 = rest
    where rest = (getEmptyRows' emptyChar (lineNum+1) lines)

getEmptyRows = getEmptyRows' '.' 0
getEmptyCols = getEmptyRows . transpose
getEmpties :: [String] -> ([Int], [Int])
getEmpties matrix = (getEmptyRows matrix, getEmptyCols matrix)

getEmptyCumsum' :: (Eq a) => a -> Int -> Int -> [[a]] -> [Int]
getEmptyCumsum' _ _ _ [] = []
getEmptyCumsum' emptyChar acc expansionFactor (line:lines)
    | emptyRow  = newAcc:rest
    | otherwise = acc:rest
    where
        newAcc
            | emptyRow  = acc+expansionFactor
            | otherwise = acc
        emptyRow = all (==emptyChar) line
        rest = getEmptyCumsum' emptyChar newAcc expansionFactor lines

getEmptyCumsum = getEmptyCumsum' '.' 0
getEmptiesCumsum expansionFactor matrix = (getEmptyCumsum expansionFactor matrix, getEmptyCumsum expansionFactor $ transpose matrix)

addExpansion :: [Int] -> [Int] -> [Int]
addExpansion expansion coordinates = expanded
    where expanded = map (\x -> x + (expansion!!x)) coordinates

pairMap :: (a -> b) -> (a, a) -> (b, b)
pairMap f (x, y) = (f x, f y)

pairDifferences :: (Num a) => [a] -> a
pairDifferences [] = 0
pairDifferences [x] = 0
pairDifferences [x,y] = abs(y-x)
pairDifferences (x:xs) = (sum $ map (\t -> abs(t-x)) xs) + pairDifferences xs

findSymbols :: (Eq a) => a -> [[a]] -> [(Int, Int)]
findSymbols = findSymbols' 0
    where
        findSymbols' :: (Eq a) => Int -> a -> [[a]] -> [(Int, Int)]
        findSymbols' _ _ [] = []
        findSymbols' index symbol (line:lines) = matches ++ rest
            where
                matches = map (\x -> (index, x)) (getIndices symbol line)
                rest = findSymbols' (index+1) symbol lines

listSum :: (Num a) => [a] -> [a] -> [a]
listSum [] [] = []
listSum (x:xs) (y:ys) = (x+y):(listSum xs ys)

getExpansionSum :: Int -> [String] -> Int
getExpansionSum expansionFactor matrix = (fst distances) + (snd distances)
    where
        distances = pairMap pairDifferences expandedCoordinates
        expandedCoordinates = (addExpansion (fst expansion) (fst rawCoordinates), addExpansion (snd expansion) (snd rawCoordinates))
        expansion = getEmptiesCumsum expansionFactor matrix
        rawCoordinates = unzip $ findSymbols '#' matrix

part1 = getExpansionSum 1
part2 = getExpansionSum (1000000-1)

{- expansionFactor:
 - Part 1: 1 (1 space -> 1+1 spaces
 - Part 2: 1000000-1.
 - Part 2 samples: 9 (1030), 99 (8410)
-}

main = do
    rawInput <- (readLines "11.in")
    putStrLn "Hello, World!"
    putStrLn $ show $ part1 rawInput
    putStrLn $ show $ part2 rawInput
