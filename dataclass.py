from dataclasses import dataclass,field

# 각 part별 DATA구조 설정
@dataclass
class Nutrition:
    EatScore: float = field(default=0.0)
    Carb: str = field(default="")
    Protein: str =field(default="")
    Fat: str =field(default="")
    Fiber: str =field(default="")
    Sodium: str =field(default="")
    Sugar: str =field(default="")
    SatFat: str =field(default="")
    Cholesterol: str =field(default="")

@dataclass
class NutritionDetail:    
    CarbH: float = field(default=0)
    CarbV: float = field(default=0)
    ProteinL: float =field(default=0)
    ProteinV: float =field(default=0)
    FatH: float =field(default=0)
    FatV: float =field(default=0)
    FiberL: float =field(default=0)
    FiberV: float =field(default=0)
    SodiumH: float =field(default=0)
    SodiumV: float =field(default=0)
    SugarH: float =field(default=0)
    SugarV: float =field(default=0)
    SatFatH: float =field(default=0)
    SatFatV: float =field(default=0)
    CholesterolH: float =field(default=0)
    CholesterolV: float =field(default=0)

@dataclass
class Supplements:
    sup1: str =field(default="")
    sup2: str =field(default="")
    sup3: str =field(default="")
    sup4: str =field(default="")
    inter1: str =field(default="")
    inter2: str =field(default="")
    inter3: str =field(default="")


@dataclass
class Vitastiq:
    Unused: bool
    Mg: str =field(default="")
    Biotin: str =field(default="")
    Se: str =field(default="")
    VitB2: str =field(default="")
    Folate: str =field(default="")
    Zn: str =field(default="")
    VitC: str =field(default="")
    VitE: str =field(default="")
    VitB6: str =field(default="")
    VitB1: str =field(default="")

@dataclass
class Inbody:
    InbodyScore: int = field(default=0)
    Weight: float = field(default=0.0)
    BMI: float= field(default=0.0)
    BodyFat: float = field(default=0.0)
    ApproWeight: float = field(default=0.0)
    FatFree: float = field(default=0.0)
    WeightControl: float = field(default=0.0)
    MuscleControl: float = field(default=0.0)
    FatControl: float = field(default=0.0)
    Recomcal: float = field(default=0.0)
    SkeletalMuscle: float = field(default=0.0)

@dataclass
class Agesensor:
    Rating: str =field(default="")
    Rank: int = field(default=0)

@dataclass
class DietGoal:
    Gweight: float = field(default=0.0)
    NMeal: int = field(default=3)    
    Rcal: float = field(default=0.0)
    Period: str =field(default="")
    FoodR: int = field(default=0)
    WorkOutR: int =field(default=0) 

@dataclass
class InbodyDetail:
    UpperLF: str =field(default="")
    UpperRF: str =field(default="")
    UpperLS: str =field(default="")
    UpperRS: str =field(default="")
    LowerLF: str =field(default="")
    LowerRF: str =field(default="")
    LowerLS: str =field(default="")
    LowerRS: str =field(default="")   

@dataclass
class SkinState:
    Concern: list
    Type: str =field(default="")
    TZWater: str =field(default="")
    UZWater: str =field(default="")
    TZOil: str =field(default="")
    UZOil: str =field(default="")
    CScore: float = field(default=0.0)
    CAScore: float = field(default=0.0)
    CState: str =field(default="")
    WScore: float = field(default=0.0)
    WAScore: float = field(default=0.0)
    WState: str =field(default="")
    TScore: float = field(default=0.0)
    TAScore: float = field(default=0.0)
    TState: str =field(default="")
    HScore: float = field(default=0.0)
    HAScore: float = field(default=0.0)
    HState: str =field(default="")
    CRank: int =field(default=0)
    WRank: int =field(default=0)
    TRank: int =field(default=0)
    HRank: int =field(default=0)