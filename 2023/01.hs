module Main
    where

import System.IO (isEOF)

isInteger :: Char -> Bool
isInteger x = isInList x "0123456789"

isInList :: Char -> [Char] -> Bool
isInList x [] = False
isInList x (a : as) = ((x == a) || (isInList x as))

getIntegers l = filter isInteger l

firstAndLastInt :: [Char] -> Integer
firstAndLastInt l = read [head (getIntegers l), last (getIntegers l)] :: Integer

readLines :: FilePath -> IO [String]
readLines = fmap lines . readFile

part1 l = sum( map firstAndLastInt l )

main = do

    rawInput <- (readLines "01.in")
    putStrLn (show (part1 rawInput))
