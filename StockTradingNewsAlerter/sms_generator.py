class SMSGenerator:
    
    # Setting default values and preparing to compose text message.
    def __init__(self, stock_symbols, percentages, article_headlines, article_briefings):
        self.stock_symbols = stock_symbols
        self.percentages = percentages
        self.article_headlines = article_headlines
        self.article_briefings = article_briefings
        self.completed_text = ""
        self.create_text()

    # Creating text message.
    def create_text(self):
        for i in range(0, len(self.percentages)):
            
            # If the percentage change for the stock is noteworthy (3% inc or dec), then send information.
            if self.percentages[i] >= 3 or self.percentages[i] <= -3:
                
                # Include arrow to indicate increase or decrease.
                if self.percentages[i] < 0.0:
                    arrow = "🔻"
                elif self.percentages[i] > 0.0:
                    arrow = "🔺"
                else:
                    arrow = "--"
                
                # Adding stock symbol, arrow, percentage.
                self.completed_text = self.completed_text + self.stock_symbols[i] + ": " + arrow + str(abs(self.percentages[i])) + "%\n\n"
                
                # Adding relevant article headings and briefings.
                for j in range(0, 3):
                    self.completed_text = self.completed_text + "Headline: " + self.article_headlines[j] + "\n"
                    self.completed_text = self.completed_text + "Briefing: " + self.article_briefings[j] + "\n\n"
                    
            # Removing headlines and briefings after passing or failing percentage check.
            self.article_headlines = self.article_headlines[3::]
            self.article_briefings = self.article_briefings[3::]
