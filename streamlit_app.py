import streamlit as st
import numpy as np
import pandas as pd

# Assignment 3
st.title("Training/Assignment - At Home\n")

# Generate Dataset of 5 Football Players
p = ["Mateo Retegui", "Lautaro Martinez", "Romelu Lukaku", "Ademola Lookman", "Marcus Thuram"]
g = np.random.randint(10, 30, size=5) # Random integer for 5 players
a = np.random.randint(10, 40, size=5)
m = np.random.randint(10, 38, size=5)
avg_d = np.random.rand(5)*20 # 5 values as players of runned distance
p_acc = np.random.rand(5)*100 # 5 percentual values of pass accuracy

d = {
    "Player Name": p,
    "Goals Scored": g,
    "Assists Made": a,
    "Matches Played": m,
    "Average Distance Covered [km]": avg_d,
    "Pass Accuracy [%]": p_acc
}

df_train = pd.DataFrame(d)

# Show created dataframe
st.subheader("Generated DataFrame")
st.dataframe(df_train)


# Charts and Interactive Elements
st.subheader("Charts and Interactive Elements")

# Goals
st.write("Goals")
st.bar_chart(df_train.set_index("Player Name")["Goals Scored"])

# Matches and Assists
st.write("Matches and Assists")
# Extraction of only interesting data in new dataframe
match_assist_data = df_train[["Player Name", "Matches Played", "Assists Made"]]
st.line_chart(match_assist_data.set_index("Player Name"))

# Accuracy and Distance Covered
st.write("Pass Accuracy and Distance Covered")
# Extraction of only interesting data in new dataframe
acc_dist_data = df_train[["Player Name", "Pass Accuracy [%]", "Average Distance Covered [km]"]]
st.area_chart(acc_dist_data.set_index("Player Name"))

# Interactive Element (Select Box)
st.write("Select a Player to View his Individual Stats")
selected_player = st.selectbox("Choose a Player (between the proposed ones)", df_train["Player Name"])
# Display Selected Player's Stats
index_selected_player = df_train["Player Name"] == selected_player # So extraction of the index (for all the columns) of the only player selected
# Creation of a new dataframe with only selected player's stats
player_stats = df_train[index_selected_player]
# Plot/Writing of the Stats of the selected player
st.write(player_stats.set_index("Player Name").T) # This command allows to report the stats on rows, no more on columns, as done in the after plotted dataframe

# Plot of its stats as a dataframe
st.write("Selected Player's Stats DataFrame")
st.dataframe(player_stats)

# Plot in a bar chart of all the stats
st.write("Selected Player Stats")
st.bar_chart(player_stats.T)