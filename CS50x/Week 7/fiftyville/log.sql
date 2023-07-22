-- Keep a log of any SQL queries you execute as you solve the mystery.

-- SELECT description, day, month, year FROM crime_scene_reports WHERE street = "Humphrey Street";
-- SELECT name,transcript FROM interviews WHERE (day = 28 AND month = 7 AND year = 2021);
-- SELECT caller, receiver, duration FROM phone_calls WHERE (day = 28 AND month = 7 AND year = 2021 AND duration < 60);
-- SELECT account_number, amount FROM atm_transactions WHERE (day = 28 AND month = 7 AND year = 2021 AND atm_location = "Leggett Street" AND transaction_type = "withdraw");
-- SELECT hour, minute , license_plate FROM bakery_security_logs WHERE (day = 28 AND month = 7 AND year = 2021 AND activity = "exit");
-- SELECT id, hour, minute, origin_airport_id, destination_airport_id FROM flights WHERE (day = 29 AND month = 7 AND year = 2021 AND origin_airport_id = (SELECT id FROM airports WHERE city = "Fiftyville"));
-- SELECT * FROM airports WHERE city = "Fiftyville";
-- SELECT name, phone_number, passport_number FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE (day = 28 AND month = 7 AND year = 2021 AND activity = "exit"));
-- SELECT name FROM people
    -- WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = "36")
-- AND name IN
    -- (SELECT name FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE (day = 28 AND month = 7 AND year = 2021 AND activity = "exit")));




-- Crime Scene Report
    -- SELECT description, day, month, year FROM crime_scene_reports WHERE (day = 28 AND month = 7 AND year = 2021 AND street = "Humphrey Street" AND description LIKE "%CS50%");

-- Interview Transcripts
    -- SELECT name,transcript FROM interviews WHERE (day = 28 AND month = 7 AND year = 2021 AND transcript LIKE "%bakery%");

-- People that left the bakery parking lot around 10:15 AM
    -- SELECT name FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE (day = 28 AND month = 7 AND year = 2021 AND hour = 10 AND minute <= 25 AND activity = "exit"));

-- People who withdrew money before 10:15 AM from ATM on Leggett Street
    -- SELECT name FROM people
        -- WHERE people.id IN (SELECT bank_accounts.person_id FROM bank_accounts WHERE bank_accounts.account_number IN (SELECT atm_transactions.account_number FROM atm_transactions WHERE (day = 28 AND month = 7 AND year = 2021 AND transaction_type = "withdraw" AND atm_location = "Leggett Street")));
-- People who were on the earliest flight out of Fiftyville on 29 July
    -- SELECT name FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = "36");

-- Calls that lasted less than a minute on 28 July
    -- SELECT name FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE (day = 28 AND month = 7 AND year = 2021 AND duration < 60));

 SELECT name FROM people WHERE phone_number IN (SELECT receiver FROM phone_calls WHERE caller = (SELECT phone_number FROM people WHERE name = "Bruce") AND duration < 60);

-- SELECT name FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id IN (SELECT id from flights WHERE (day = 29 AND month = 7 AND year = 2021)));