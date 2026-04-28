def calculate_dc(racks, kw_per_rack):
    total_kw = racks * kw_per_rack
    ups_kva = total_kw / 0.95
    rt = (total_kw * 860) / 3024
    flow = total_kw * 0.86

    return {
        "Total_kW": round(total_kw,2),
        "UPS_kVA": round(ups_kva,2),
        "Cooling_RT": round(rt,2),
        "Flow_LPM": round(flow,2)
    }
