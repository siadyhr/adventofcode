module Main
    where

import Data.Map (Map)
import qualified Data.Map as Map
import MyAOCLib

rawToCard :: String -> ([Int], [Int])
rawToCard s = (map read leftHalf, map read rightHalf)
    where
    [leftHalfRaw, rightHalfRaw]   = split '|' dataString
    leftHalf = [x | x <- split ' ' leftHalfRaw, x /= ""]
    rightHalf = [x | x <- split ' ' rightHalfRaw, x /= ""]
    dataString = (split ':' s)!!1

getCardPoints :: ([Int], [Int]) -> Int
getCardPoints (winningNumbers, card) =
    if nWinningNumbers == 0 then 0 else 2^(nWinningNumbers-1)
    where
    nWinningNumbers = length myWins
    myWins = filter (`elem` winningNumbers) card

part1 :: [String] -> Int
part1 s = sum $ map getCardPoints (map rawToCard s)

main = do
    rawInput <- (readLines "04.in")
    putStrLn "Hello, World!"
    putStrLn $ show $ rawToCard (rawInput!!0)
    putStrLn $ show $ getCardPoints $ rawToCard (rawInput!!0)
    putStrLn $ show $ part1 rawInput
