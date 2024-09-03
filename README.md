# DA Points

## Commands

    elm make src/Main.elm --output=main.js

## Data API

https://rapidapi.com/slashgolf/api/live-golf-data

## Database Design

Draft
Id UserId TournamentId PlayerId

Player
Id Name

Round
Id TournamentId PlayerId Score

Tournament
Id Name StartTimestamp StopTimestamp

Users
Id Name Email Password

