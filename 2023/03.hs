module Main
    where

import Data.Map (Map)
import qualified Data.Map as Map
import MyAOCLib

isIn :: (Eq a) => a -> [a] -> Bool
isIn a [] = False
isIn a (b:tail) = (a == b || a `isIn` tail)

isSymbol :: Char -> Bool
isSymbol c = (c /= '.') && (not (c `isIn` ['0'..'9']))

getNeighbouredNumbersRaw :: String -> Bool -> String -> String -> String -> [String]
getNeighbouredNumbersRaw currentString valid "" "" ""
    | valid     = [currentString]
    | otherwise = []

getNeighbouredNumbersRaw currentString valid (s0:previous) (s:current) (s1:next)
    | s `isIn` ['0'..'9']   = getNeighbouredNumbersRaw (currentString ++ [s]) newValid previous current next
    | otherwise             = [completeString] ++ getNeighbouredNumbersRaw "" nextValid previous current next
    where   newValid = valid || nextValid
            completeString = if newValid then currentString else ""
            nextValid = (isSymbol s0) || (isSymbol s) || (isSymbol s1)

getNeighbouredNumbers = getNeighbouredNumbersRaw "" False

blankPad :: Char -> [String] -> [String]
blankPad c l = blank ++ l ++ blank
    where   blank = [take n (repeat c)]
            n = length (l!!0)

rawNeighbouringNumbersToNumbers :: [String] -> [Int]
rawNeighbouringNumbersToNumbers l = [read x | x<-l, x/=""]

dotPad = blankPad '.'

tripleifyGrid :: [String] -> [((String, String), String)]
tripleifyGrid grid = zip (zip paddedGrid grid) (tail $ tail paddedGrid)
    where paddedGrid = dotPad grid

part1 :: [String] -> Int
part1 inputMap = sum [sum line | line <- validNumbers]
    where   validNumbers = map rawNeighbouringNumbersToNumbers rawValidNumbers
            rawValidNumbers = [getNeighbouredNumbers a b c | ((a, b), c) <- tripleifyGrid inputMap]

main = do
    rawInput <- (readLines "03.in")
    putStrLn $ show $ part1 rawInput
