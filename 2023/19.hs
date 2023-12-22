--{-# OPTIONS_GHC -Wall #-}
module Main
    where

import Data.Map (Map)
import qualified Data.Map as Map
import MyAOCLib

part2 x = ""

parse :: [String] -> (Map String (Map Char Int -> String), [Map Char Int])
parse rawInput = (workFlows, parts)
    where
        workFlows = Map.fromList $ map parseWorkflow rawWorkFlows
        parts = map parsePart rawParts
        [rawWorkFlows, rawParts] = split "" rawInput

parsePart :: String -> Map Char Int
parsePart rawInput = Map.fromList $ zip "xmas" rawValues
    where
        rawValues = map (read . drop 2) splittedValues
        splittedValues = split ',' (drop 1 (take (length rawInput - 1) rawInput))

{- Take a line
 - px{a<2006:qkq,m>2090:A,rfg}
 - and return (px, f), where f evaluates
 - an element based the rule a<2006 -> qkq
 - and so on
 -}
parseWorkflow :: String -> (String, Map Char Int -> String)
parseWorkflow rawInput = (label, rule)
    where
        rule = ruleListToRule ruleList
        rawRuleToSingleRule :: String -> (Map Char Int -> Maybe String)
        -- Case: Final rule with no condition
        rawRuleToSingleRule rawRule
            | not $ ':' `elem` rawRule    = \x -> Just rawRule
        -- Case: Rule with conditions
        rawRuleToSingleRule rawRule
            | condition == '<'  = \x -> if (Map.findWithDefault 0 letter x) < value then Just nextLabel else Nothing
            | condition == '>'  = \x -> if (Map.findWithDefault 0 letter x) > value then Just nextLabel else Nothing
            | otherwise         = error "invalid condition"
            where
                [(letter:condition:rawValue),nextLabel] = split ':' rawRule
                value = read rawValue :: Int

        ruleList = map rawRuleToSingleRule rawRuleList
        ruleListToRule :: [(Map Char Int -> Maybe String)] -> (Map Char Int -> String)

        -- The last rule should give something
        ruleListToRule [rule] element = case (rule element) of
            Just x -> x
            Nothing -> error "no default rule"
        ruleListToRule (rule:rules) element = case (rule element) of
            Just result -> result
            Nothing     -> ruleListToRule rules element

        rawRuleList = split ',' rawRuleString
        [label, rawRuleString] = split '{' (take (length rawInput - 1) rawInput)

scoreElem :: Map Char Int -> Int
scoreElem = Map.foldl (+) 0

evaluateElement :: Map String (Map Char Int -> String) -> Map Char Int -> Int
evaluateElement workFlow element = evaluateElement' "in" workFlow element

evaluateElement' :: String -> Map String (Map Char Int -> String) -> Map Char Int -> Int
evaluateElement' label workFlows element
    | nextLabel == "A"  = scoreElem element
    | nextLabel == "R"  = 0
    | otherwise         = evaluateElement' nextLabel workFlows element
    where
        maybeWorkFlow = Map.lookup label workFlows
        workFlow = getJustPartial maybeWorkFlow
        nextLabel = workFlow element

part1 x = sum $ map (evaluateElement workFlows) elements
    where
        (workFlows, elements) = parse x

main = do
    rawSampleInput <- (readLines "19sample.in")
    rawInput <- (readLines "19.in")

    putStrLn "Part 1"
    putStrLn $ show $ part1 $ rawSampleInput
    putStrLn $ show $ part1 $ rawInput

    putStrLn "Part 2"
    putStrLn $ show $ part2 $ rawSampleInput
    putStrLn $ show $ part2 $ rawInput
