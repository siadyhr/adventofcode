--{-# OPTIONS_GHC -Wall #-}
module Main
    where

import Data.Map (Map)
import qualified Data.Map as Map
import MyAOCLib

{-
data BinaryTree a = Leaf a | Branch (BinaryTree a) (BinaryTree a) a deriving (Show)

x :: BinaryTree String
x = Branch (Branch (Leaf "A") (Leaf "A2") "A'") (Leaf "B") "C"

parse :: [String] -> ([String], BinaryTree)
parse s = 
    where
        instructions    = cycle $ head s
        rawNodes        = drop 2 s
        rawNodeToBranch :: String -> Branch
        rawNodeToBranch s = Branch 
-}

parse :: [String] -> (String, Map String (String, String))
parse s = (instructions, tree)
    where
        tree            = Map.fromList $ map parseLine rawNodes
        instructions    = cycle $ head s
        rawNodes        = drop 2 s
        parseLine :: [a] -> ([a], ([a], [a]))
        parseLine ss = (nodeName, (leftNode, rightNode))
            where
                nodeName    = take 3 ss
                leftNode    = take 3 $ drop 7 ss
                rightNode   = take 3 $ drop 12 ss

findAndCountRaw :: Int -> Map String (String, String) -> String -> String -> String -> Int
findAndCountRaw n tree startLabel endLabel (direction:directions)
    | startLabel == endLabel    = n
    | direction == 'L'          = findAndCountRaw (n+1) tree left endLabel directions
    | direction == 'R'          = findAndCountRaw (n+1) tree right endLabel directions
    where
        (left, right) = defaultLookup startLabel ("0", "0") tree

findAndCount :: Map String (String, String) -> String -> String -> String -> Int
findAndCount = findAndCountRaw 0


defaultLookup key defaultValue mapping =
    case result of
        Nothing -> defaultValue
        Just a  -> a
    where result = Map.lookup key mapping

findSuffixAndCountRaw :: Int -> Map String (String, String) -> [String] -> Char -> String -> Int
findSuffixAndCountRaw n tree startLabels endSuffix (direction:directions)
    | all (==True) $ map (\x -> (x!!2) == endSuffix) startLabels  = n
    | direction == 'L'          = findSuffixAndCountRaw (n+1) tree leftLabels endSuffix directions
    | direction == 'R'          = findSuffixAndCountRaw (n+1) tree rightLabels endSuffix directions
    where
        leftLabels = map fst keyLookups
        rightLabels = map snd keyLookups
        keyLookups = map (\x -> defaultLookup x ("0", "0") tree) startLabels

findSuffixAndCount :: Map String (String, String) -> [String] -> Char -> String -> Int
findSuffixAndCount = findSuffixAndCountRaw 0

findLabelsWithSuffix :: Char -> Map String (String, String) -> [String]
findLabelsWithSuffix suffix tree = filter (\x -> (x!!2 == suffix)) (Map.keys tree)

part1 :: [String] -> Int
part1 s = findAndCount tree "AAA" "ZZZ" directions
    where
        (directions, tree) = parse s

part2 :: [String] -> Int
part2 s = findSuffixAndCount tree startLabels 'Z' directions
    where
        (directions, tree) = parse s
        startLabels = findLabelsWithSuffix 'A' tree

main = do
    rawInput <- (readLines "08.in")
    putStrLn "Hello, World!"
    putStrLn $ show $ part1 rawInput
    putStrLn $ show $ part2 rawInput
