# src/core/gst_logic.py

def get_citizen_advice_by_industry(industry: str) -> dict:
    """
    Takes a business industry string and returns the expected GST rate
    and a simple piece of advice for a citizen.

    
    """
    # Normalize the industry string to lowercase for easier matching
    industry_lower = industry.lower()

    # --- This is our "Rule Engine" ---
    # We will add more and more rules here over time.

    # Rule for Restaurants & Food
    if "restaurant" in industry_lower or "cafe" in industry_lower or "food" in industry_lower:
        return {
            "expected_gst_rate": "5% (without Input Tax Credit)",
            "citizen_advice": "Check your bill. For dine-in or takeaway, you should only be charged 5% GST. This GST is not split into CGST + SGST."
        }

    # Rule for Electronics & Durables
    if "electronics" in industry_lower or "appliance" in industry_lower or "computer" in industry_lower:
        return {
            "expected_gst_rate": "18%",
            "citizen_advice": "Most electronics and appliances fall under the 18% GST slab."
        }

    # Rule for IT, Consulting, Services
    if "it services" in industry_lower or "consulting" in industry_lower or "telecom" in industry_lower or "bpo" in industry_lower:
        return {
            "expected_gst_rate": "18%",
            "citizen_advice": "Most services, like software, consulting, and phone bills, attract 18% GST."
        }

    # Rule for Retail / General Stores
    if "retail" in industry_lower or "general store" in industry_lower:
        return {
            "expected_gst_rate": "Varies (0%, 5%, 12%, 18%)",
            "citizen_advice": "Kiranas or retail stores sell many items. Unpackaged food is 0%, but packaged/branded items, soaps, etc., are 5% or 12%."
        }

    # Rule for Automobiles
    if "automotive" in industry_lower or "automobile" in industry_lower:
        return {
            "expected_gst_rate": "28% + Cess",
            "citizen_advice": "Cars are in the highest tax slab of 28% and also have an additional 'Cess' based on the car's size and engine."
        }

    # Default fallback rule
    return {
        "expected_gst_rate": "N/A",
        "citizen_advice": "Could not determine a specific GST rate for this business type."
    }


# --- PART 2: THE NEW "MASTER FUNCTION" (ADD THIS) ---

from src.validators.unified_validator import validate_input
from src.apis.gst_simulator import simulate_gst_api_call

def get_full_gst_details(validation_result : dict) -> dict:
    """
    This is the new "master" function that runs the entire process.
    """
    
    
    # 2. If the format is invalid, stop and return the error
    if not validation_result["valid"]:
        return validation_result
        
    # 3. If format is valid, call the simulator to get "real" data
    simulated_data = simulate_gst_api_call(validation_result.get("input"))
    
    # 4. Get the citizen advice using our other function
    advice_data = get_citizen_advice_by_industry(simulated_data["business_type"])
    
    # 5. Combine everything into one final, powerful response
    final_response = {
        "gstin": simulated_data["gstin"],
        "status": simulated_data["status"],
        "legal_name": simulated_data["legal_name"],
        "business_type": simulated_data["business_type"],
        "expected_gst_rate": advice_data["expected_gst_rate"],
        "citizen_advice": advice_data["citizen_advice"],
        "validation_message": validation_result.get("message", "GSTIN dtail retrieval successful.")
    }
    
    return final_response

