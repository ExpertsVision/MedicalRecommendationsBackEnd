QUERIES = {
"GetAgeRecommendations": "SELECT  title, grade, recomend_text, serv_freq, risk_text, rationale, general, tool_0, tool_1, tool_2 FROM epss_db.epss_finaldata WHERE  (gender=%s or gender=%s or gender=%s) and (risk_name=%s or risk_name=%s or risk_name=%s or risk_name=%s or risk_name=%s);",
"GetAGSTPRecommendations":"SELECT title, grade, recomend_text, serv_freq, risk_text, rationale, general, tool_0, tool_1, tool_2 FROM epss_db.epss_finaldata WHERE (%s between agerange0 and agerange1) and (gender=%s or gender=%s) and (risk_name=%s or risk_name=%s or risk_name=%s or risk_name=%s or risk_name=%s );",
"GetRecommendations":"SELECT title, grade, recomend_text, serv_freq, risk_text, rationale, general, tool_0, tool_1, tool_2 FROM epss_db.epss_finaldata WHERE (%s between agerange0 and agerange1) and (gender=%s or gender=%s or gender=%s) and (risk_name=%s or risk_name=%s or risk_name=%s or risk_name=%s or risk_name=%s);",
"GetAGRecommendations":"SELECT title, grade, recomend_text, serv_freq, risk_text, rationale, general, tool_0, tool_1, tool_2 FROM epss_db.epss_finaldata WHERE (gender=%s or gender=%s) and (risk_name=%s or risk_name=%s or risk_name=%s or risk_name=%s or risk_name=%s);",
"GetGeneralData":"SELECT  clinical, clinicalurl, Other, discussion, rationale, title, topic FROM epss_db.generaldata WHERE id=%s;",
"GetToolsData":"SELECT  title, url_list FROM epss_db.tools WHERE (id=%s or id=%s or id=%s)",
"GetAllRecommendations":"SELECT title, grade, recomend_text, serv_freq, risk_text, rationale, general, tool_0, tool_1, tool_2, grade_version, gender, agerange0,agerange1, id,source FROM epss_db.epss_finaldata;",
"AddRecomendations":"INSERT INTO epss_db.epss_finaldata(title, gender, grade, grade_version, risk_text, "
"agerange0,agerange1,serv_freq,recomend_text,source) "
"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
"DeleteRecomendations":"DELETE FROM epss_db.epss_finaldata where id=%s;",
"EditRecomendations":"UPDATE epss_db.epss_finaldata SET title=%s,gender=%s,grade=%s,grade_version=%s, "
"agerange0=%s, agerange1=%s,serv_freq=%s, risk_text=%s,source=%s,recomend_text=%s WHERE id=%s;",
"AdminLoginCheck":"SELECT EXISTS(SELECT admin_email,admin_password FROM epss_db.admin WHERE admin_email=%s and admin_password=%s);",
"AdminLoginUpdate":"INSERT INTO epss_db.admin (admin_email,admin_password) VALUES(%s, %s);"
}