﻿using System.Net.Http;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.Web;

namespace phone_exchange_2_dot_net.REST
{
    public static class Helper
    {
        public static async Task<T> HttpGetAsync<T>(string url, int timeoutSeconds)
        {
            HttpClient HttpClient = new HttpClient();
            HttpClient.Timeout = TimeSpan.FromSeconds(timeoutSeconds);
            using var httpResponse = await HttpClient.GetAsync(url).ConfigureAwait(false);
            httpResponse.EnsureSuccessStatusCode();
            var stream = await httpResponse.Content.ReadAsStreamAsync().ConfigureAwait(false);
            return JsonSerializer.Deserialize<T>(stream)!;
        }

        public static T HttpGet<T>(string url, int timeoutSeconds)
        {
            using var httpClient = new HttpClient 
            { 
                Timeout = TimeSpan.FromSeconds(timeoutSeconds) 
            };

            using var request = new HttpRequestMessage(HttpMethod.Get, url);
            using HttpResponseMessage response = httpClient
                .SendAsync(request)
                .GetAwaiter()
                .GetResult();
            response.EnsureSuccessStatusCode();
            using Stream responseStream = response.Content
                .ReadAsStreamAsync()
                .GetAwaiter()
                .GetResult();
            var options = new JsonSerializerOptions
            {
                PropertyNameCaseInsensitive = true
            };
            object? obj = JsonSerializer.Deserialize(responseStream, typeof(T), options);
            T result = (T)obj!;
            return result;
        }

        public static string UrlEncode(string value) => HttpUtility.UrlEncode(value ?? string.Empty);
    }
}
