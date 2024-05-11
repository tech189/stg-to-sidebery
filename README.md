# How to use
1. Go to your Simple Tab Groups settings and save a backup file (Settings>Backup your Simple Tab Groups>Create backup)
2. Disable/remove the addon
3. Install Sidebery
4. Go to Sidebery's settings and save a snapshot (Settings>Snapshots viewer>Create snapshot)
5. Save the Python file in this repository (`convert_stg_to_sidebery.py`)
7. Run it by providing the paths to where the STG backup file and the Sidebery snapshot are stored:
    ```sh
    python3 convert_stg_to_sidebery.py \
        --simple-tab-groups-backup "path/to/stg-backup.json" \
        --sidebery-snapshot "path/to/sidebery-snapshot.json"
    ```
   The output will be saved to wherever you ran the Python file
8. Import the generated `sidebery-output.json` in Sidebery (Settings>Snapshots viewer>Import snapshot)
9. Once loaded, click on the imported snapshot in the list and then click `Open window` on the right
10. A new window opens with all your tabs sorted again - **this may take 20 seconds or so with e.g. 500+ tabs**
11. Close the old unsorted window
12. You may want to turn on "Hide native tabs of inactive panels" to get the same experience as Simple Tab Groups
