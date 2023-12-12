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

getEmptyCumsum' :: (Eq a) => a -> Int -> [[a]] -> [Int]
getEmptyCumsum' _ _ [] = []
getEmptyCumsum' emptyChar acc (line:lines)
    | emptyRow  = newAcc:rest
    | otherwise = acc:rest
    where
        newAcc
            | emptyRow  = acc+1
            | otherwise = acc
        emptyRow = all (==emptyChar) line
        rest = getEmptyCumsum' emptyChar newAcc lines

getEmptyCumsum = getEmptyCumsum' '.' 0
getEmptiesCumsum matrix = (getEmptyCumsum matrix, getEmptyCumsum $ transpose matrix)

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

part1 :: [String] -> Int
part1 matrix = (fst distances) + (snd distances)
    where
        distances = pairMap pairDifferences expandedCoordinates
        expandedCoordinates = (addExpansion (fst expansion) (fst rawCoordinates), addExpansion (snd expansion) (snd rawCoordinates))
        expansion = getEmptiesCumsum matrix
        rawCoordinates = unzip $ findSymbols '#' matrix

main = do
    rawInput <- (readLines "11.in")
    putStrLn "Hello, World!"
    putStrLn $ show $ part1 rawInput
