--{-# OPTIONS_GHC -Wall #-}
module Main
    where

import MyAOCLib

parse :: [String] -> [[String]]
parse = split []

findReflectionPoints :: [String] -> [Int]
findReflectionPoints matrix = foldl findReflectionPointsAt [1..lineLength] matrix
    where
        lineLength = (length (matrix!!0)) - 1

        findReflectionPointsAt :: [Int] -> String -> [Int]
        findReflectionPointsAt [] _ = []
        findReflectionPointsAt searchPoints line = [x | x <- searchPoints, isMirroredAt x line]

        isMirroredAt :: (Eq a) => Int -> [a] -> Bool
        isMirroredAt splitPoint list = all (==True) $ map (\(x, y) -> x==y) $ zip left right
            where
                right = drop splitPoint list
                left = reverse $ take splitPoint list

getReflectionScore :: [String] -> Int
getReflectionScore matrix
    | not $ null reflectCols    = reflectCols!!0
    | otherwise                 = 100 * (reflectRows!!0)
    where
        reflectCols = findReflectionPoints matrix
        reflectRows = findReflectionPoints $ transpose matrix

part1 :: [[String]] -> Int
part1 = sum . map getReflectionScore

main = do
    rawSampleInput <- (readLines "13sample.in")
    rawInput <- (readLines "13.in")

    putStrLn "Hello, World!"
    putStrLn $ show $ (parse rawSampleInput)!!0
    putStrLn $ show $ part1 $ parse $ rawSampleInput
    putStrLn $ show $ part1 $ parse $ rawInput
