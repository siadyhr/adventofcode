--{-# OPTIONS_GHC -Wall #-}
module Main
    where

import MyAOCLib

calculateLoad :: [String] -> Int
calculateLoad matrix = combineWeights (length matrix) matrix
    where
        combineWeights _ [] = 0
        combineWeights weight (row:rows) = weight * (calculateLoad row) + combineWeights (weight - 1) rows
        calculateLoad row = (countOccurences 'O' row)

tiltRight :: [String] -> [String]
tiltRight matrix = map tiltRightRow matrix
    where
        tiltRightRow :: String -> String
        tiltRightRow "" = ""
        tiltRightRow [x] = [x]
        tiltRightRow (x:y:xs)
            | x == '.'              = '.':(tiltRightRow (y:xs))
            | x == 'O' && y == '.'  = '.':'O':tiltRightRow xs

{- Calculates the weight after tilting _up_
 - We transpose the matrix so we can tilt
 - the board row-wise (towards the head)
 -}
calculateTiltedLoad :: [String] -> Int
calculateTiltedLoad matrix = sum $ map calculateTiltedLoadRow (transpose matrix)
    where
        calculateTiltedLoadRow :: String -> Int
        calculateTiltedLoadRow x = calculateTiltedLoadRow' (length x) (length x) x
        calculateTiltedLoadRow' :: Int -> Int -> String -> Int
        calculateTiltedLoadRow' _ _ [] = 0
        calculateTiltedLoadRow' n _ [x]
            | x == 'O'  = n
            | otherwise = 0
        calculateTiltedLoadRow' n r (x:xs)
            | x == 'O'  = n + calculateTiltedLoadRow' (n-1) (r-1) xs
            | x == '.'  = calculateTiltedLoadRow' n (r-1) xs
            | x == '#'  = calculateTiltedLoadRow' (r-1) (r-1) xs

part1 = calculateTiltedLoad
part2 x = ""

main = do
    rawSampleInput2 <- (readLines "14sample2.in")
    rawInput <- (readLines "14.in")

    putStrLn "Hello, World!"
    putStrLn $ show $ part1 $ rawSampleInput2
    putStrLn $ show $ part1 $ rawInput

    putStrLn $ show $ part2 $ rawSampleInput2
    putStrLn $ show $ part2 $ rawInput
