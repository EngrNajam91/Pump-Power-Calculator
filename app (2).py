import gradio as gr

def pump_power(density, flow_rate, head, efficiency):
    try:
        g = 9.81  # m/s²

        # Convert flow rate from m³/hr to m³/s
        flow_m3s = flow_rate / 3600  

        # Hydraulic power
        ph = density * g * flow_m3s * head  

        # Actual shaft power (W)
        p = ph / efficiency  

        # Convert to kW and HP
        p_kw = p / 1000
        p_hp = p / 745.7  

        return (
            f"🔹 Hydraulic Power: {ph/1000:.2f} kW\n"
            f"🔹 Pump Shaft Power: {p_kw:.2f} kW\n"
            f"🔹 Pump Shaft Power: {p_hp:.2f} HP"
        )

    except Exception as e:
        return f"❌ Error: {str(e)}"

with gr.Blocks() as demo:
    gr.Markdown("## ⚙️ Pump Power Calculator")
    gr.Markdown("Calculate pump power for given fluid properties and conditions.")

    with gr.Row():
        density = gr.Number(label="Fluid Density (kg/m³)", value=1000)
        flow_rate = gr.Number(label="Flow Rate (m³/hr)", value=100)
    
    with gr.Row():
        head = gr.Number(label="Pump Head (m)", value=50)
        efficiency = gr.Slider(label="Pump Efficiency (0-1)", minimum=0.1, maximum=1.0, value=0.7, step=0.01)

    output = gr.Textbox(label="Result", lines=4)

    btn = gr.Button("Calculate Pump Power")
    btn.click(fn=pump_power, inputs=[density, flow_rate, head, efficiency], outputs=output)

if __name__ == "__main__":
    demo.launch()
