import numpy as np

class Agent:
    STATE_DIM = 2
    
    TRADING_CHARGE = 0
    TRADING_TAX = 0
    
    ACTION_BUY = 0
    ACTION_SELL = 1
    ACTION_HOLD = 2
    ACTIONS = [ACTION_BUY, ACTION_SELL]
    NUM_ACTIONS = len(ACTIONS)
    
    def __init__(self, environment, min_trading_unit=1, max_trading_unit=2, delayed_reward_threshold=.05):
        self.environment = environment
        
        self.min_trading_unit = min_trading_unit
        self.max_trading_unit = max_trading_unit
        self.delayed_reward_threshold = delayed_reward_threshold
        
        self.initial_balance = 0
        self.balance = 0
        self.num_stocks = 0
        self.portfolio_value = 0
        self.base_portfolio_value = 0
        self.num_buy = 0
        self.num_sell = 0
        self.num_hold = 0
        self.immediate_reward = 0
        
        self.ratio_hold = 0
        self.ratio_portfolio_value = 0
        
    def reset(self):
        self.balance = self.initial_balance
        self.num_stocks = 0
        self.portfolio_value = self.initial_balance
        self.base_portfolio_value = self.initial_balance
        self.num_buy = 0
        self.num_sell = 0
        self.num_hold = 0
        self.immediate_reward = 0
        self.ratio_hold = 0
        self.ratio_portfolio_value = 0
        
    def set_balance(self, balance):
        self.initial_balance = balance
        
    def get_states(self):
        self.ratio_hold = self.num_hold / int(self.portfolio_value / self.environment.get_price())
        self.ratio_portfolio_value = self.portfolio_value / self.initial_balance
        return (
            self.ratio_hold,
            self.ratio_portfolio_value
        )