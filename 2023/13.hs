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

findReflectionFailures :: (Eq a) => [[a]] -> [[Int]]
findReflectionFailures = map findReflectionFailures'
    where
        findReflectionFailures' :: (Eq a) => [a] -> [Int]
        findReflectionFailures' list = [countFailuresAt x list | x <- [1..length list - 1]]
            where
                countFailuresAt :: (Eq a) => Int -> [a] -> Int
                countFailuresAt index list = sum $ map (\(x, y) -> if x /= y then 1 else 0) $ zip left right
                    where
                        right = drop index list
                        left = reverse $ take index list

getSmudgeScore :: [String] -> Int
getSmudgeScore matrix = if reflects then reflectionIndex + 1 else 100*(reflectionIndex + 1)
    where
        reflectionIndex = if reflects then getFirstIndex 1 (fst reflectionFailures) else getFirstIndex 1 (snd reflectionFailures)
        reflects = 1 `elem` (fst reflectionFailures)
        reflectionFailures = (
                                combineFailures $ findReflectionFailures matrix,
                                combineFailures $ findReflectionFailures $ transpose matrix)

combineFailures :: [[Int]] -> [Int]
combineFailures [] = []
combineFailures [line] = line
combineFailures (line1:line2:lines) = combineFailures ((map (\(x, y) -> x+y) $ zip line1 line2):lines)

--part2 matrices = map (combineFailures . findReflectionFailures . transpose) matrices
part2 matrices = sum $ map getSmudgeScore matrices

main = do
    rawSampleInput <- (readLines "13sample.in")
    rawInput <- (readLines "13.in")

    putStrLn "Hello, World!"
    putStrLn $ show $ (parse rawSampleInput)!!0
    putStrLn $ show $ part1 $ parse $ rawSampleInput
    putStrLn $ show $ part1 $ parse $ rawInput

    putStrLn $ show $ part2 $ parse $ rawSampleInput
    putStrLn $ show $ part2 $ parse $ rawInput
