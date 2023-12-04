--{-# OPTIONS_GHC -Wall #-}
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
    nWinningNumbers = getNWinningNumbers (winningNumbers, card)

getNWinningNumbers :: ([Int], [Int]) -> Int
getNWinningNumbers (winningNumbers, card) =
    length $ filter (`elem` winningNumbers) card

elongateLeft :: Int -> a -> [a] -> [a]
elongateLeft 0 _ l = l
elongateLeft n a l
    | n <= 0    = l
    | otherwise = elongateLeft (n-1) a (a:l)

elongate :: Int -> a -> [a] -> [a]
elongate n a l = reverse $ elongateLeft n a (reverse l)

oplus :: (Num a) => [a] -> [a] -> [a]
oplus [] l = l
oplus l [] = l
oplus (x:xs) (y:ys) = (x+y):(oplus xs ys)

otimes :: Int -> [a] -> [a]
otimes 0 _ = []
otimes n l = l ++ (otimes (n-1) l)

part2Work :: [([Int], [Int])] -> [Int] -> Int
part2Work [] _ = 0
part2Work [card] [n] =
    n
part2Work (card:stack) (n:ns) =
    n + (part2Work stack (oplus ns (otimes nWins [n])))
    where nWins = getNWinningNumbers card

part1 :: [String] -> Int
part1 s = sum $ map getCardPoints (map rawToCard s)

part2 :: [String] -> Int
part2 s = part2Work (map rawToCard s) (otimes (length s) [1])

main = do
    rawInput <- (readLines "04.in")
    putStrLn "Hello, World!"
    putStrLn $ show $ rawToCard (rawInput!!0)
    putStrLn $ show $ getCardPoints $ rawToCard (rawInput!!0)
    putStrLn "Part 1"
    putStrLn $ show $ part1 rawInput
    putStrLn "Part 2"
    putStrLn $ show $ part2 rawInput
