def calculate_discount(price, discount_percent):
        if discount_percent >= 20:
            final_price = price - (price * discount_percent / 100)
            return final_price
        else:
             return price
        
        def main():
    # Prompt user for input
         price = float(input("Enter the original price of the item: "))
         discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate the final price using the calculate_discount function
         final_price = calculate_discount(price, discount_percent)
    
    # Print the final price
         if final_price == price:
           print(f"No discount applied. The price is {final_price}.")
         else:
           print(f"The final price after applying the discount is {final_price}.")

# Run the main function
        main()
        
 