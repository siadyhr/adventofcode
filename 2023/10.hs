--{-# OPTIONS_GHC -Wall #-}
module Main
    where

import Data.Map (Map)
import qualified Data.Map as Map
import MyAOCLib

findCoordinate :: Char -> [String] -> (Int, Int)
findCoordinate label [] = error $ (show label) ++ " not found"
findCoordinate label (line:lines) = (row, col)
    where
        (row, col)
            | label `elem` line = (0, labelCol)
            | otherwise         = (1+(fst search), snd search)
        search = findCoordinate label lines
        labelCol = getFirstIndex label line

findStartCoordinate = findCoordinate 'S'

{- neighbourOne is the first matching character
 - looking North, East, South, neighbourTwo is
 - the first matching looking West, South, East.
 -}
getNeighbours :: [String] -> (Int, Int) -> [((Int, Int), Char)]
getNeighbours labyrinth (x, y) = [neighbourOne, neighbourTwo]
    where
        neighbourOne
            | charN `elem` "7|FS"    = ((-1, 0), charN)
            | charE `elem` "J-7S"    = ((0, 1), charE)
            | charS `elem` "J|LS"    = ((1, 0), charS)
        neighbourTwo
            | charW `elem` "L-FS"    = ((0, -1), charW)
            | charS `elem` "J|LS"    = ((1, 0), charS)
            | charE `elem` "J-7S"    = ((0, 1), charE)
        charN = labyrinth!!(x-1)!!y
        charS = labyrinth!!(x+1)!!y
        charE = labyrinth!!x!!(y+1)
        charW = labyrinth!!x!!(y-1)

characterToDirections :: Char -> [(Int, Int)]
characterToDirections x
    | x == '|'  = [(-1, 0), (1, 0)]
    | x == '-'  = [(0, -1), (0, 1)]
    | x == '7'  = [(0, -1), (1, 0)]
    | x == 'F'  = [(0, 1),  (1, 0)]
    | x == 'J'  = [(-1, 0), (0, -1)]
    | x == 'L'  = [(-1, 0), (0, 1)]
    | x == '.'  = error "Tried to walk outside"

coordSum :: (Num a) => (a, a) -> (a, a) -> (a, a)
coordSum (x1, y1) (x2, y2) = (x1+x2, y1+y2)

coordMult :: (Num a) => a -> (a, a) -> (a, a)
n `coordMult` (x, y) = (n*x, n*y)

nextStep :: [String] -> (Int, Int) -> (Int, Int) -> (Int, Int)
nextStep labyrinth (x, y) fromDirection = toDirection
    where
        toDirection = head $ filter (/= fromDirection) possibleDirections
        possibleDirections = characterToDirections currentCharacter
        currentCharacter = labyrinth!!x!!y

navigate :: [String] -> (Int, Int) -> (Int, Int) -> [(Char, (Int, Int))]
navigate labyrinth start fromDirection = output
    where
        output = [(newCharacter, newLocation)] ++ continuedNavigation
        continuedNavigation = navigate labyrinth newLocation newFromDirection
        newCharacter = labyrinth!!(fst newLocation)!!(snd newLocation)
        newFromDirection = (-1) `coordMult` step
        newLocation = start `coordSum` step
        step = nextStep labyrinth start fromDirection

takeUntil :: (Eq a) => (a -> Bool) -> [a] -> [a]
takeUntil _ [] = []
takeUntil f (x:xs)
    | not $ f x = x:(takeUntil f xs)
    | otherwise = [x]

part1 :: [String] -> Int
part1 labyrinth = circuitLength `div` 2
    where
        circuitLength = 1 + length circuit
        circuit = takeUntil (\x -> fst x == 'S') navigation
        navigation = navigate labyrinth firstStepCoords fromDirection
        -- startNeighbours = [(direction, symbol)]
        fromDirection = (-1) `coordMult` firstDirection
        firstStepCoords = startCoord `coordSum` firstDirection
        firstDirection = fst $ startNeighbours!!0
        startNeighbours = getNeighbours labyrinth startCoord
        startCoord = findStartCoordinate labyrinth
        
main = do
    rawInput <- (readLines "10.in")
    putStrLn "Hello, World!"
    putStrLn $ show $ part1 rawInput
