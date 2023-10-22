#include <iostream>
#include <curl/curl.h>
#include <nlohmann/json.hpp>

// Function to translate text using Google Translate API
std::string translate_text(const std::string& text, const std::string& source_lang, const std::string& target_lang) {
    std::string url = "https://translation.googleapis.com/language/translate/v2?key=YOUR_API_KEY";
    url += "&q=" + text;
    url += "&source=" + source_lang;
    url += "&target=" + target_lang;

    CURL* curl = curl_easy_init();
    std::string response;

    if (curl) {
        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, [](void* buffer, size_t size, size_t count, void* stream) {
            ((std::string*)stream)->append((char*)buffer, 0, size * count);
            return size * count;
        });
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &response);
        CURLcode res = curl_easy_perform(curl);

        if (res != CURLE_OK) {
            std::cerr << "Failed to perform HTTP request: " << curl_easy_strerror(res) << std::endl;
        }

        curl_easy_cleanup(curl);
    }

    // Extract translation from JSON response
    nlohmann::json json_response = nlohmann::json::parse(response);
    return json_response["data"]["translations"][0]["translatedText"].get<std::string>();
}

int main() {
    std::string source_language = "en";  // English
    std::string target_language = "es";  // Spanish
    std::string text_to_translate = "Hello, how are you?";
    std::string translated_text = translate_text(text_to_translate, source_language, target_language);
    std::cout << "Translated: " << translated_text << std::endl;
    return 0;
}