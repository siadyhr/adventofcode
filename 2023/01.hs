module Main
    where

import Data.Map (Map)
import qualified Data.Map as Map
import Data.Maybe (fromJust, isJust)

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

wordToIntList = zip ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] [0..9]
wordToInt = Map.fromList wordToIntList
reverseWordToInt = Map.fromList [(reverse x, y) | (x, y) <- wordToIntList]

getFirstInteger :: String -> Map String Int -> Int
getFirstInteger (x:_) _
    | isInteger x = (read [x])
getFirstInteger x dict
    | Map.member (take 3 x) dict = fromJust (Map.lookup (take 3 x) dict)
    | Map.member (take 4 x) dict = fromJust (Map.lookup (take 4 x) dict)
    | Map.member (take 5 x) dict = fromJust (Map.lookup (take 5 x) dict)
getFirstInteger x dict = getFirstInteger (tail x) dict

getLastInteger :: String -> Int
getLastInteger x = getFirstInteger(reverse x) reverseWordToInt

getFirstAndLastIntegerPart2 x = read ( show (getFirstInteger x wordToInt) ++ show (getLastInteger x) ) :: Int

part2 l = sum ( map getFirstAndLastIntegerPart2 l )

main = do
    rawInput <- (readLines "01.in")
    putStrLn (show (part1 rawInput))
    putStrLn (show (part2 rawInput))
    putStrLn (show (getFirstAndLastIntegerPart2 (rawInput !! 1)))
