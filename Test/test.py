#import the Quant Lib
import QuantLib as ql


# Let the today date whenwe want to value a instrument be
today = ql.Date(15,6,2020)

# we can set evaluationDate in QL as
ql.Settings.instance().evaluationDate = today
print(ql.Settings.instance().evaluationDate);
# prints..June 15th, 2020

# or you can do
today = ql.Date(15,12,2021);
ql.Settings.instance().setEvaluationDate(today)
print(ql.Settings.instance().evaluationDate)
# prints..December 15th, 2021

settlementDays = 2

# Holiday calendar of United States
calendar = ql.UnitedStates(ql.UnitedStates.NYSE)


forwardRate = 0.05

"""Day Counter provides methods for determining the length of a time period according to given market convention,
both as a number of days and as a year fraction."""
dayCounter = ql.Actual360()

# Construct flat forward rate term structure
flatForwardTermStructure = ql.FlatForward(settlementDays, calendar, forwardRate, dayCounter)

flatForwardTermStructure.referenceDate()

print("Max Date: ", flatForwardTermStructure.maxDate())

today = ql.Date(15,6,2020)
ql.Settings.instance().evaluationDate = today

effectiveDate = ql.Date(15, 6, 2020)
terminationDate = ql.Date(15, 6, 2022)

schedule = ql.MakeSchedule(effectiveDate, terminationDate, ql.Period('6M'))

notional = 100.0
rate = 0.05
leg = ql.FixedRateLeg(schedule, dayCounter, [notional], [rate])

dayCounter = ql.Thirty360(ql.Thirty360.BondBasis)
rate = 0.03

compoundingType = ql.Compounded

frequency = ql.Annual
interestRate = ql.InterestRate(rate, dayCounter, compoundingType, frequency)

ql.Settings.instance().evaluationDate = ql.Date(15,12,2020)
yts = ql.YieldTermStructureHandle(ql.FlatForward(ql.Date(15,1,2020),
                                                 0.04,
                                                 ql.Actual360()))

print( ql.CashFlows.npv(leg, yts, True) )
