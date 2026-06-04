// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract StudentScore {

    mapping(string => string)
        private scoreHashes;

    event HashStored(
        string key,
        string hashValue
    );

    function addScoreHash(
        string memory key,
        string memory hashValue
    )
        public
    {
        scoreHashes[key] = hashValue;

        emit HashStored(
            key,
            hashValue
        );
    }

    function getScoreHash(
        string memory key
    )
        public
        view
        returns (
            string memory
        )
    {
        return scoreHashes[key];
    }
}