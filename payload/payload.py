valid_create_payload = {
   "name": "Apple MacBook Pro 11111",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": 'Intel Core i9',
      "Hard disk size": "1 TB"
   }
}

invalid_create_payload = {
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 'dfdf',
      "price": 1849.99,
      "CPU model": 'Intel Core i9',
      "Hard disk size": "1 TB"
   }

}


valid_update_payload = {
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": 'Intel Core i9',
      "Hard disk size": "1 TB",
      "color": "red"
   }
}


invalid_update_payload = {
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": 'Intel Core i9',
      "Hard disk size": "1 TB",
      "color": 13
   }
}