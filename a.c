
if ((dbg_pkt_fp = fopen(DEBUG_PKT_DUMP, "r"))) {
        fclose(dbg_pkt_fp);
        dbg_pkt_fp = NULL;
    }